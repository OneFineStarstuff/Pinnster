import hashlib
import json
import os
from datetime import datetime

class PQCWORMLogger:
    def __init__(self, audit_dir="audit"):
        self.audit_dir = audit_dir
        if not os.path.exists(audit_dir):
            os.makedirs(audit_dir)
        self.last_hash = "0" * 128 # Genesis block hash

    def _generate_hash(self, data):
        # Using SHA3-512 (Keccak) for PQC-readiness
        hasher = hashlib.sha3_512()
        hasher.update(data.encode('utf-8'))
        return hasher.hexdigest()

    def log_batch(self, batch_data):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        batch_id = f"WORM_{timestamp}"

        entry = {
            "batch_id": batch_id,
            "timestamp": datetime.now().isoformat(),
            "data": batch_data,
            "prev_hash": self.last_hash
        }

        content = json.dumps(entry, sort_keys=True)
        current_hash = self._generate_hash(content)
        entry["hash"] = current_hash

        filename = os.path.join(self.audit_dir, f"{batch_id}.json")
        with open(filename, 'w') as f:
            json.dump(entry, f, indent=2)

        self.last_hash = current_hash
        return filename

if __name__ == "__main__":
    logger = PQCWORMLogger()
    print(f"Logged: {logger.log_batch({'event': 'test_audit_pulse'})}")
