#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET

def main():
  try:
    tree = ET.parse(sys.argv[1])  
  except:
    print(f"Usage:\n  {sys.argv[0]} filename.fpl [WAYPOINT_PREFIX]")
    sys.exit(1)
  root = tree.getroot()
  if root.tag.endswith("flight-plan"):
    namespace = root.tag[root.tag.index("{"):root.tag.index("}")+1]
    print(f"Namespace: {namespace}")
    print(f"Got {root.tag}")
  else:
    print(f"Unknown tree: {root.tag}")
    sys.exit(1)

  wprefix = None
  if len(sys.argv) > 2:
    wprefix = sys.argv[2]

  for child in root:
    if child.tag.endswith("waypoint-table"):
      ofilename = f"{sys.argv[1]}.csv"
      print("Found waypoint-table")
      print(f"Writing {ofilename}")
      with open(ofilename, "w") as ofile:
        for waypoint in child:
          if waypoint.find(namespace+"type").text == "USER WAYPOINT":
            name = waypoint.find(namespace+"identifier").text
            if wprefix:
              name = wprefix + name[2:]
            lat = waypoint.find(namespace+"lat").text
            lon = waypoint.find(namespace+"lon").text
            ofile.write(f"{name.upper()},,{lat},{lon}\r\n")
      print("Done.")
      break
  else:
    print("No waypoint-table found.")

if __name__ == "__main__":
  main()
