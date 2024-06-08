#!/usr/bin/env zsh
# CSS hard-stop gradient generator
# https://css-tricks.com/books/greatest-css-tricks/hard-stop-gradients/

zmodload zsh/mathfunc

gradient_stops() {
    percent_step=$(( 100. / $# ))
    stops=()
    for ((x=0;x<=$#;x++)) {
        stops+=$(( floor(percent_step * x + 0.5) ))
    }
    for ((x=1;x<${#stops};x++)) {
        print ${(P)x} ${stops[$x]:s/./%/}, ${(P)x} ${stops[$((x+1))]:s/./%/},
    }
}

cssify() {
    iinput="$(cat)"
    setopt HIST_SUBST_PATTERN
    cat <<CSS
background-image: linear-gradient(
    to bottom,
${iinput%,}
);
CSS
}

if (( $# == 0 )); then
    print "No arguments! If you're writing the colours in CSS notation with a hash/number sign in front, you have to quote them so that the shell doesn't interpret them as comments."
else
    gradient_stops $@ | cssify
fi
