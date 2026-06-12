import unittest
from engine.zk_fairness_prover import ZKFairnessProver
from engine.asa_interpretability import ASAInterpretabilityLayer

class TestCompliance(unittest.TestCase):
    def setUp(self):
        self.zk_prover = ZKFairnessProver(target_parity_threshold=0.05)
        self.interpretability_layer = ASAInterpretabilityLayer()

    def test_zk_fairness_proof_generation(self):
        telemetry = {"node": "retail_moe_01"}
        proof = self.zk_prover.generate_fairness_proof(telemetry)

        self.assertEqual(proof["proof_type"], "ZK-SNARK (Demographic Parity)")
        self.assertEqual(proof["standard"], "MAS FEAT")
        self.assertIn("parity_delta", proof)
        self.assertIn("is_compliant", proof)
        self.assertIn("proof_commitment", proof)

    def test_cae_envelope_generation(self):
        score = 25.5
        status = "GREEN"
        pulse = {"risk_delta": 1.2}
        cae = self.interpretability_layer.generate_cae(score, status, pulse)

        self.assertEqual(cae["standard"], "HKMA Ethics")
        self.assertIn("cae_id", cae)
        self.assertIn("attributions", cae)
        self.assertGreaterEqual(cae["coverage_score"], 0.95)

        # Verify attributions sum to ~1.0
        total_attribution = sum(cae["attributions"].values())
        self.assertAlmostEqual(total_attribution, 1.0, places=4)

if __name__ == "__main__":
    unittest.main()
