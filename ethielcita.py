"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""
#sudo mn --custom Topologia.py --topo Red1 --controller remote --switch ovsk --mac
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        hostA = self.addHost( 'hA', mac = '00:00:00:00:00:01' )
        hostB = self.addHost( 'hB', mac = '00:00:00:00:00:02' )
        hostC = self.addHost( 'hC', mac = '00:00:00:00:00:03' )
        hostD = self.addHost( 'hD', mac = '00:00:00:00:00:04' )
        hostE = self.addHost( 'hE', mac = '00:00:00:00:00:05' )
        hostF = self.addHost( 'hF', mac = '00:00:00:00:00:06' )
        switchX = self.addSwitch( 's1', dpid = '1' )
        switchY = self.addSwitch( 's2', dpid = '2' )
        switchZ = self.addSwitch( 's3', dpid = '3' )

        # Add links
        self.addLink( hostA, switchX, 1, 10)
        self.addLink( hostB, switchX, 2, 11)
        self.addLink( hostC, switchY, 3, 12)
        self.addLink( hostD, switchY, 4, 13)
        self.addLink( hostE, switchZ, 5, 14)
        self.addLink( hostF, switchZ, 6,  15)
        self.addLink( switchX, switchY, 7, 16)
        self.addLink( switchX, switchZ, 8, 17)
        self.addLink( switchY, switchZ, 9, 18)

topos = { 'MyTopo': ( lambda: MyTopo() ) }
