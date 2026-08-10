puts "Connecting"
connect
puts "Choosing Target"
target 1
puts "Flashing (will take about 2 to 3min)"
set current_dir [pwd]
set path [lindex $argv 0]
set process [open "|program_flash -f $path  -flash_type is25lp032d-spi-x1_x2_x4 -blank_check -verify -cable type xilinx_tcf url tcp:localhost:3121" r ]
puts process

while {[gets $process line] >= 0} { puts $line }
if {[catch {close $process} result options]} {
   if {[lindex [dict get $options -errorcode] 0] eq "CHILDSTATUS"} {
       return [lindex [dict get $options -errorcode] 2]
   } else {
       # Rethrow other errors
       return -options [dict incr options -level] $result
   }
}
puts "Flashing finished"
