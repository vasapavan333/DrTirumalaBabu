/* Dr. Manchikalapudi Tirumala Babu — site behaviour.
   Vanilla, no dependencies. Everything here is progressive enhancement:
   with JavaScript off the page is fully readable and every link still works. */

(function () {
  "use strict";

  var WHATSAPP_NUMBER = "918985014488"; // clinic WhatsApp, digits only
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- mobile navigation ------------------------------------------------ */

  var toggle = document.querySelector(".nav__toggle");
  var panel = document.getElementById("nav-panel");

  function closeNav() {
    if (!toggle || !panel) return;
    toggle.setAttribute("aria-expanded", "false");
    panel.classList.remove("is-open");
    panel.hidden = true;
  }

  if (toggle && panel) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      panel.classList.toggle("is-open", !open);
      panel.hidden = open;
    });

    panel.addEventListener("click", function (e) {
      if (e.target.closest("a")) closeNav();
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeNav();
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth >= 900) closeNav();
    });
  }

  /* ---- sticky header shadow --------------------------------------------- */

  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-stuck", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---- active section in the nav ---------------------------------------- */

  var navLinks = Array.prototype.slice.call(
    document.querySelectorAll(".nav__list a[href^='#']")
  );
  var sections = navLinks
    .map(function (link) {
      var id = link.getAttribute("href").slice(1);
      return id ? document.getElementById(id) : null;
    })
    .filter(Boolean);

  function markCurrent(id) {
    navLinks.forEach(function (link) {
      if (link.getAttribute("href") === "#" + id) {
        link.setAttribute("aria-current", "true");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  }

  if ("IntersectionObserver" in window && sections.length) {
    var spy = new IntersectionObserver(
      function (entries) {
        // Near the top of the page "Home" is the honest answer, whatever
        // section happens to overlap the sticky header.
        if (window.scrollY < 320) {
          markCurrent("top");
          return;
        }
        entries.forEach(function (entry) {
          if (entry.isIntersecting && entry.target.id !== "top") {
            markCurrent(entry.target.id);
          }
        });
      },
      { rootMargin: "-45% 0px -50% 0px" }
    );
    sections.forEach(function (section) {
      spy.observe(section);
    });
    window.addEventListener(
      "scroll",
      function () {
        if (window.scrollY < 320) markCurrent("top");
      },
      { passive: true }
    );
    markCurrent("top");
  }

  /* ---- reveal on scroll (subtle, opt-out on reduced motion) -------------- */

  var revealTargets = document.querySelectorAll(
    ".section__head, .card, .pillar, .step, .conditions li, .panel, .trust__item"
  );

  if (!reduceMotion && "IntersectionObserver" in window) {
    Array.prototype.forEach.call(revealTargets, function (el) {
      el.classList.add("reveal");
    });
    var revealer = new IntersectionObserver(
      function (entries, observer) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );
    Array.prototype.forEach.call(revealTargets, function (el) {
      revealer.observe(el);
    });

    // Failsafe: content must never stay invisible because an observer did not
    // fire (print, screenshot tools, scripted scrolling, odd browsers).
    var revealAll = function () {
      Array.prototype.forEach.call(revealTargets, function (el) {
        el.classList.add("is-visible");
      });
    };
    window.setTimeout(revealAll, 4000);
    window.addEventListener("beforeprint", revealAll);
  }

  /* ---- click-to-load map ------------------------------------------------- */
  /* The Google Maps iframe is only requested once the visitor asks for it, so
     the page does not pay for a third-party frame on first load. */

  var facade = document.querySelector(".map-facade");
  if (facade) {
    facade.addEventListener("click", function () {
      var frame = document.createElement("iframe");
      frame.className = "map-frame";
      frame.src = facade.getAttribute("data-map");
      frame.title = "Map showing Maruthi Hospital and Diagnostics, Guntur";
      frame.loading = "lazy";
      frame.referrerPolicy = "no-referrer-when-downgrade";
      frame.setAttribute("allowfullscreen", "");
      facade.replaceWith(frame);
    });
  }

  /* ---- appointment enquiry ---------------------------------------------- */
  /* There is no backend. The form composes a WhatsApp message the visitor
     sends themselves, so nothing is collected or stored by this website. */

  var form = document.getElementById("appointment-form");
  if (form) {
    var status = form.querySelector(".form__status");

    form.addEventListener("submit", function (e) {
      e.preventDefault();

      var name = form.elements.name.value.trim();
      var phone = form.elements.phone.value.trim();

      if (!name || !phone) {
        if (status) status.textContent = "Please add your name and phone number.";
        (name ? form.elements.phone : form.elements.name).focus();
        return;
      }

      var date = form.elements.date.value;
      var who = form.elements.for.value;
      var message = form.elements.message.value.trim();

      var lines = [
        "Appointment enquiry — Dr. Tirumala Babu",
        "Name: " + name,
        "Phone: " + phone,
      ];
      if (date) lines.push("Preferred date: " + date);
      if (who) lines.push("Consultation for: " + who);
      if (message) lines.push("Message: " + message);

      var url =
        "https://wa.me/" +
        WHATSAPP_NUMBER +
        "?text=" +
        encodeURIComponent(lines.join("\n"));

      if (status) {
        status.textContent =
          "Opening WhatsApp — press send there to reach the clinic.";
      }
      window.open(url, "_blank", "noopener");
    });
  }
})();
