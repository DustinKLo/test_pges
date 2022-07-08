import os
import random
import json

rand_ints = ''.join(random.choice([str(i) for i in range(10)]) for i in range(13))
state_config_id = 'dtid_%s_state-config' % rand_ints  # dtid_0123456789123_state-config

if not os.path.exists(state_config_id):
    os.mkdir(state_config_id)


dataset_json = {
    "version": "2.0",
    "ldf_name": "{}.ldf".format(state_config_id),
    "missing_rrsts": [],
    "found_rrsts": [],
    "rrst_product_paths": [],
    "state": "job-completed",
}


dataset_json_file = os.path.join(state_config_id, "%s.dataset.json" % state_config_id)
with open(dataset_json_file, 'w') as f:
    json.dump(dataset_json, f, indent=2)

met_json_file = os.path.join(state_config_id, "%s.met.json" % state_config_id)
with open(met_json_file, 'w') as f:
    json.dump({}, f)
