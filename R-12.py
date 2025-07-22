from jnpr.junos import Device
from jnpr.junos.utils.config import Config

with Device(host='30.0.0.61', user='root', passwd='Juniper') as dev:
	with Config(dev) as cu:
		cu.load("set interfaces em0 unit 0 family inet address 192.168.2.2/24", format="set")
		cu.load("set interfaces lo0 unit 0 family inet address 12.12.12.13/32", format="set")
		cu.load("set interfaces lo0 unit 0 family inet address 12.12.12.14/32", format="set")
		cu.load("set interfaces lo0 unit 0 family inet address 12.12.12.15/32", format="set")
		cu.load("set interfaces lo0 unit 0 family inet address 12.12.12.16/32", format="set")
		cu.load("set interfaces lo0 unit 0 family inet address 12.12.12.17/32", format="set")
		cu.load("set interfaces lo0 unit 0 family inet address 12.12.12.18/32", format="set")
		cu.load("set interfaces lo0 unit 0 family inet address 12.12.12.19/32", format="set")
		cu.load("set interfaces lo0 unit 0 family inet address 12.12.12.20/32", format="set")
		cu.load("set routing-options autonomous-system 300", format="set")
		cu.load("set protocols bgp group AS300-100 type external", format="set")
		cu.load("set protocols bgp group AS300-100 peer-as 100", format="set")
		cu.load("set protocols bgp group AS300-100 neighbor 192.168.2.1 peer-as 100", format="set")
		cu.load("set protocols bgp group AS300-100 export EXPORTAR", format="set")
		cu.load("set policy-options policy-statement EXPORTAR term 1 from interface lo0.0", format="set")
		cu.load("set policy-options policy-statement EXPORTAR term 1 then accept", format="set")
		cu.load("set system host-name R-12", format="set")
		cu.pdiff()
		cu.commit()
		print("Configuración de la interfaz aplicada con éxito.")	
