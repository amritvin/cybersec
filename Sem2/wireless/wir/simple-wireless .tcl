set val(chan)           Channel/WirelessChannel    ;# channel type
set val(prop)           Propagation/TwoRayGround   ;# radio-propagation model
set val(netif)          Phy/WirelessPhy            ;# network interface type
set val(mac)            Mac/802_11                 ;# MAC type
set val(ifq)            Queue/DropTail/PriQueue    ;# interface queue type
set val(ll)             LL                         ;# link layer type
set val(ant)            Antenna/OmniAntenna        ;# antenna model
set val(ifqlen)         50                         ;# max packet in ifq
set val(nn)             10                          ;# number of mobilenodes
set val(rp)             DSDV                       ;# routing protocol

# ======================================================================
# Main Program
# ======================================================================


#
# Initialize Global Variables
#
set ns_	[new Simulator]
set nf [open simple.nam w]
set tracefd [open trace.tr w]
$ns_ trace-all $tracefd
$ns_ namtrace-all-wireless $nf 1 1

# set up topography object
set topo       [new Topography]

$topo load_flatgrid 50 50

#
# Create God
#
create-god $val(nn)

#
#  Create the specified number of mobilenodes [$val(nn)] and "attach" them
#  to the channel. 
#  Here two nodes are created : node(0) and node(1)

# configure node

        $ns_ node-config -adhocRouting $val(rp) \
			 -llType $val(ll) \
			 -macType $val(mac) \
			 -ifqType $val(ifq) \
			 -ifqLen $val(ifqlen) \
			 -antType $val(ant) \
			 -propType $val(prop) \
			 -phyType $val(netif) \
			 -channelType $val(chan) \
			 -topoInstance $topo \
			 -agentTrace ON \
			 -routerTrace ON \
			 -macTrace OFF \
			 -movementTrace OFF			
			 
	for {set i 0} {$i < $val(nn) } {incr i} {
		set node_($i) [$ns_ node]	
		$node_($i) random-motion 0		;# disable random motion
	}

#
# Provide initial (X,Y, for now Z=0) co-ordinates for mobilenodes
#
$node_(0) set X_ 45.0
$node_(0) set Y_ 45.0
$node_(0) set Z_ 0.0

$node_(1) set X_ 75.0
$node_(1) set Y_ 45.0
$node_(1) set Z_ 0.0

$node_(2) set X_ 135.0
$node_(2) set Y_ 45.0
$node_(2) set Z_ 0.0


$node_(3) set X_ 45.0
$node_(3) set Y_ 65.0
$node_(3) set Z_ 0.0


$node_(4) set X_ 45.0
$node_(4) set Y_ 25.0
$node_(4) set Z_ 0.0


$node_(5) set X_ 35.0
$node_(5) set Y_ 35.0
$node_(5) set Z_ 0.0


$node_(6) set X_ 55.0
$node_(6) set Y_ 35.0
$node_(6) set Z_ 0.0


$node_(7) set X_ 35.0
$node_(7) set Y_ 35.0
$node_(7) set Z_ 0.0


$node_(8) set X_ 55.0
$node_(8) set Y_ 35.0
$node_(8) set Z_ 0.0


$node_(9) set X_ 100.0
$node_(9) set Y_ 100.0
$node_(9) set Z_ 0.0



#
# Now produce some simple node movements
# Node_(1) starts to move towards node_(0)
#
#$ns_ at 50.0 "$node_(1) setdest 25.0 20.0 15.0"
$ns_ at 50.0 "$node_(2) setdest 40.0 30.0 20.0"
$ns_ at 10.0 "$node_(0) setdest 20.0 25.0 30.0"

# Node_(1) then starts to move away from node_(0)
#$ns_ at 10.0 "$node_(1) setdest 49.0 48.0 15.0" 
$ns_ initial_node_pos $node_(1) 10
$ns_ initial_node_pos $node_(2) 10
$ns_ initial_node_pos $node_(0) 10
$ns_ initial_node_pos $node_(3) 10
$ns_ initial_node_pos $node_(4) 10
$ns_ initial_node_pos $node_(5) 10
$ns_ initial_node_pos $node_(6) 10
$ns_ initial_node_pos $node_(7) 10
$ns_ initial_node_pos $node_(8) 10
$ns_ initial_node_pos $node_(9) 10
# Setup traffic flow between nodes
# TCP connections between node_(0) and node_(1)

set tcp [new Agent/TCP]
$tcp set class_ 2
set sink [new Agent/TCPSink]
$ns_ attach-agent $node_(0) $tcp
$ns_ attach-agent $node_(1) $sink
$ns_ connect $tcp $sink
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ns_ at 10.0 "$ftp start" 

set tcp [new Agent/TCP]
$tcp set class_ 2
set sink [new Agent/TCPSink]
$ns_ attach-agent $node_(1) $tcp
$ns_ attach-agent $node_(2) $sink
$ns_ connect $tcp $sink
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ns_ at 10.0 "$ftp start" 
#
# Tell nodes when the simulation ends
#
for {set i 0} {$i < $val(nn) } {incr i} {
    $ns_ at 150.0 "$node_($i) reset";
}
$ns_ at 150.0 "stop"
$ns_ at 150.01 "puts \"NS EXITING...\" ; $ns_ halt"
proc stop {} {
    global ns_ nf
    $ns_ flush-trace
    close $nf
    exec nam simple.nam &
    exit 0
}

puts "Starting Simulation..."
$ns_ run

