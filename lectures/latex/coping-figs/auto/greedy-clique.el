(TeX-add-style-hook
 "greedy-clique"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("color" "usenames" "dvips")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "graphicx"
    "color"
    "amsmath"
    "amssymb"
    "times"
    "subfig")
   (TeX-add-symbols
    "SpaceChar")))

