from jnpr.junos import Device
from jnpr.junos.utils.config import Config

with Device(host='30.0.0.58', user='root', passwd='Juniper') as dev:
	with Config(dev) as cu:
		cu.load("set interfaces em0 unit 0 family inet address 17.0.0.2/24", format="set")
		cu.load("set interfaces em1 unit 0 family inet address 18.0.0.1/24", format="set")
		cu.load("set interfaces em1 unit 0 family inet address 22.0.0.2/24", format="set")
		cu.load("set protocols ospf area 0 interface em0.0", format="set")
		cu.load("set protocols ospf area 0 interface em1.0", format="set")
		cu.load("set protocols ospf area 0 interface em2.0", format="set")
		cu.load("set protocols ospf traffic-engineering", format="set")
		cu.load("set interfaces em0 unit 0 family mpls", format="set")
		cu.load("set interfaces em1 unit 0 family mpls", format="set")
		cu.load("set interfaces em2 unit 0 family mpls", format="set")
		cu.load("set protocols mpls interface em0.0", format="set")
		cu.load("set protocols mpls interface em1.0", format="set")
		cu.load("set protocols mpls interface em2.0", format="set")
		cu.load("set protocols mpls icmp-tunneling", format="set")
		cu.load("set protocols rsvp interface em0.0", format="set")
		cu.load("set protocols rsvp interface em1.0", format="set")
		cu.load("set protocols rsvp interface em2.0", format="set")
		cu.load("set system host-name R-9", format="set")
		cu.pdiff()
		cu.commit()
		print("Configuración de la interfaz aplicada con éxito.")
