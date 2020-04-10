(TeX-add-style-hook
 "approxVC-example"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("color" "usenames" "dvips")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "gastex"
    "color"
    "amsmath"
    "amssymb"
    "times")
   (TeX-add-symbols
    "SpaceChar")))

