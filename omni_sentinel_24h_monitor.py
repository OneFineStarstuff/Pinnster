import time
import logging
import os
from engine.u_gamma_single import UGammaSingle
from engine.gsri_scoring_engine import GSRIScoringEngine
from engine.pqc_worm_logger import PQCWORMLogger
from engine.zk_fairness_prover import ZKFairnessProver
from engine.asa_interpretability import ASAInterpretabilityLayer

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("OmniSentinel")

def run_monitor():
    cognitive_engine = UGammaSingle()
    risk_engine = GSRIScoringEngine()
    audit_logger = PQCWORMLogger()
    zk_prover = ZKFairnessProver()
    interpretability_layer = ASAInterpretabilityLayer()

    logger.info("Omni-Sentinel 24h Monitoring Environment Online.")

    while True:
        try:
            # 1. Pulse Cognitive Engine
            pulse = cognitive_engine.pulse()

            # 2. Score G-SRI
            score = risk_engine.calculate_score(pulse)

            # 3. Verify thresholds
            status = "GREEN" if risk_engine.is_safe() else "RED"

            # 4. Attestation Check (Simulated)
            pcr_match = "TRUE" # PCR_MATCH=TRUE

            # 5. Generate Compliance Proofs
            zk_proof = zk_prover.generate_fairness_proof({"score": score})
            cae_envelope = interpretability_layer.generate_cae(score, status, pulse)

            log_entry = {
                "g_sri": score,
                "status": status,
                "pcr_match": pcr_match,
                "pulse": pulse,
                "zk_fairness_proof": zk_proof,
                "cae_envelope": cae_envelope
            }

            # 6. Commit to WORM Audit
            audit_file = audit_logger.log_batch(log_entry)

            logger.info(f"Checkpoint: G-SRI={score} | Status={status} | Audit={audit_file}")

            if status == "RED":
                logger.warning(f"THRESHOLD VIOLATION: G-SRI {score} exceeds limit!")

            # Simulate 15-minute intervals (shortened for initial verification in real run)
            # In production this would be 900 seconds.
            time.sleep(60)

        except Exception as e:
            logger.error(f"Monitoring Error: {str(e)}")
            time.sleep(10)

if __name__ == "__main__":
    run_monitor()
