set term postscript eps color
set xrange[1:10]
set output 'wait.eps'
set ylabel 'wait'
set xlabel 'time'
plot 'p4.txt' using 1:2 with linespoints ls 1
