# Pushing the eight commits

This session cannot push to `github.com/vasapavan333/DrTirumalaBabu`. The git
proxy in front of it refuses to supply a credential for a repository that is
not in the session's authorized set — it is a permission on this session, not
a problem with your repository or your credentials:

```
remote: access denied by the git proxy: vasapavan333/DrTirumalaBabu is not in
this session's authorized repository set
```

So the work is on your computer instead. Pick whichever of these suits you.

---

## Option A — one commit, simplest

Everything is already in your `DrTirumalaBabu` folder. **First delete these
two files** — this session can write files on your computer but not delete
them, so they are still there and nothing references either:

```
assets\fonts\noto-telugu.woff2
tools\content_te.py
```

Then, from that folder:

```bash
git add -A
git commit -m "Condition, therapy and service pages; accordion lists; nav dropdowns; Telugu; gallery"
git push
```

You lose the eight-commit history but the end state is identical.

---

## Option B — keep the eight commits

`drtb-claude-work.bundle` sits in the same folder. It carries the eight
commits and nothing else, and it applies on top of `2deff8f`, which you
already have.

Your working tree currently holds exactly the same changes as the bundle, so
discard them first — nothing is lost, the bundle puts them back as commits:

```bash
cd "C:\Users\PavanVasa\OneDrive - IBM\Personal\DAN\DrTirumalaBabu"

git status                       # confirm you have no edits of your own
git stash push -u                # only if you do have edits of your own
git checkout -- .                # discard the working-tree copy
git clean -fd                    # remove the new untracked pages

git fetch drtb-claude-work.bundle main:claude-work
git merge --ff-only claude-work
git branch -d claude-work
git push
```

Afterwards `git log --oneline -9` should read:

```
544a840 Remove all Telugu, and the illustrative-images note
9a7045a Say "Follow us on Instagram", and put the link on every page
eb3b2cc Add an Instagram link to the hero name chip
7d6c937 Add the clinic gallery and a Telugu layer; stop the image build breaking the hero
1b44a66 Restore the original header lockup, take the width from the nav instead
6ca92f1 Add a page for every condition, therapy and service; nav dropdowns
db9d584 Turn services, conditions and therapies into accordion lists
2b8b42f Add condition and therapy pages, repair structured data
2deff8f Initial website launch
```

Delete the bundle once it is pushed.

---

## Option C — authorize this session

Add `vasapavan333/DrTirumalaBabu` to this session's sources and I will push
directly next time. That also makes future changes a single step rather than
this hand-off.

---

## Before you push

Serve the folder over http and click through it — `preview.cmd`, or
`python -m http.server 4181`. Never open `index.html` by double-clicking it:
browsers block webfonts on `file://` and the page silently falls back to
system faces, which looks broken and is not.

Worth a look specifically:

- the three dropdowns in the header, on a wide window
- the hamburger menu on a narrow one, including the collapsible groups
- a few of the new pages, reached by opening a row on Services, Conditions or
  Therapies and following the link
- the Telugu subtitles, which should render as Telugu rather than as boxes

And the one thing that is not a technical matter: **none of the clinical copy
on the 36 generated pages has been read by Dr. Tirumala Babu.**
`TODO-CONTENT.md` §11 lists which file holds which text, and the four specific
questions worth putting to him.
