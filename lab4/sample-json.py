import json 

json_file = r"C:\Users\User\Desktop\pp2\lab4\sample.json"
json_data = {}
with open(json_file) as file:
    json_data = json.load(file)

def parse_json(data):
    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
    print("-" * 80)
    for item in data["imdata"]:
        attributes = item["l1PhysIf"]["attributes"]
        dn = attributes["dn"]
        description = attributes.get("descr", "")
        speed = attributes.get("speed", "inherit")
        mtu = attributes.get("mtu", "")
        print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")

parse_json(json_data)
