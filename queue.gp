#plots queue vs time from p3.txt
set term postscript eps color
set output 'queue.eps'
set ylabel 'queue'
set xlabel 'time'
plot 'p3.txt' using 1:2 with linespoints ls 1
