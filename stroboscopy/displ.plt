while (1) {
  stats "/tmp/pixel" nooutput
  first = (STATS_records > 40) ? STATS_records - 39 : 1
  set xlabel "time"
  set ylabel "position"
  set grid
  set yrange [-5 : 5]
  pause 1
  plot "/tmp/pixel" every ::first-1 using 0:1 with linespoints title "Data"
}
