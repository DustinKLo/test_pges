import os
import json

dataset_json = {
  "version": "2.0",
  "label": "Oregon",
  "location": {
    "type": "polygon",
    "coordinates": [
      [
        [-123.99169921875, 46.14939437647686],
        [-123.96972656249999, 45.644768217751924],
        [-124.21142578125, 43.8503744993026],
        [-124.5849609375, 42.89206418807337],
        [-124.23339843749999, 42.049292638686836],
        [-117.00439453125, 42.01665183556825],
        [-116.78466796875, 44.02442151965934],
        [-117.861328125, 45.321254361171476],
        [-119.72900390625001, 45.920587344733654],
        [-122.32177734375, 45.61403741135093],
        [-122.89306640624999, 46.10370875598026],
        [-123.99169921875, 46.14939437647686]
      ]
    ]
  },
  "starttime": "2022-07-01T00:00:00"
}

dataset_id = "AOI_Oregon"
if not os.path.exists(dataset_id):
    os.mkdir(dataset_id)


dataset_json_file = os.path.join(dataset_id, "%s.dataset.json" % dataset_id)
with open(dataset_json_file, 'w') as f:
    json.dump(dataset_json, f, indent=2)

met_json_file = os.path.join(dataset_id, "%s.met.json" % dataset_id)
with open(met_json_file, 'w') as f:
    json.dump({}, f)


