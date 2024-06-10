#!/usr/bin/env zsh

print "/* Code auto-generated by timegen.sh */"

for halve in AM PM; do
for hour in 12 1 2 3 4 5 6 7 8 9 10 11; do
if [[ $halve == AM && $hour -eq 12 ]]; then
print "/* End at 12:00 AM */"
cat <<CSS
.schedule > .end-12am {
    grid-row-end: 27;
}
CSS
nostart=0
noend=1
else
nostart=0
noend=0
fi

halvn=0
if [[ $halve == PM ]] halvn=12

printf "/* %02d:00 %s */\n" $hour $halve
rownum=$(((hour % 12 + halvn)+2))
if ((nostart == 0)); then
cat <<CSS
.schedule > .start-${hour}${(L)halve} {
    grid-row-start: ${rownum};
}
CSS
fi; if ((noend == 0)); then
cat <<CSS
.schedule > .end-${hour}${(L)halve} {
    grid-row-end: ${rownum};
}
CSS
fi
done
done
