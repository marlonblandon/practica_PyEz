from jnpr.junos import Device
from jnpr.junos.utils.config import Config

with Device(host='30.0.0.60', user='root', passwd='Juniper') as dev:
	with Config(dev) as cu:
		cu.load("set interfaces em0 unit 0 family inet address 192.168.1.2/24", format="set")
		cu.load("set interfaces lo0 unit 0 family inet address 11.11.11.11/32", format="set")
		cu.load("set routing-options autonomous-system 200", format="set")
		cu.load("set protocols bgp group AS200-100 type external", format="set")
		cu.load("set protocols bgp group AS200-100 peer-as 100", format="set")
		cu.load("set protocols bgp group AS200-100 neighbor 192.168.1.1 peer-as 100", format="set")
		cu.load("set policy-options policy-statement EXPORTAR term 1 from interface lo0.0", format="set")
		cu.load("set policy-options policy-statement EXPORTAR term 1 then accept", format="set")
		cu.load("set system host-name R-11", format="set")
		cu.pdiff()
		cu.commit()
		print("Configuración de la interfaz aplicada con éxito.")
