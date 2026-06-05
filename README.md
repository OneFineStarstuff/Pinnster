# Omni-Sentinel Cognitive Execution Environment

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![G-SRI Safety](https://img.shields.io/badge/G--SRI-Stable-green)](https://github.com/onefinestarstuff/omni-sentinel)

Omni-Sentinel is a verifiable, hardware-anchored containment and governance framework designed for AGI/ASI entities. It ensures systemic risk mitigation through cryptographic proof, post-quantum resistant audit trails, and real-time behavioral monitoring.

## 🚀 Vision
To establish a future-proof ecosystem where artificial intelligence operates within verifiable safety boundaries, anchored by a Hardware Root of Trust (HRoT).

## 🛠 Features

- **G-SRI Scoring Engine**: Real-time Systemic Risk Index calculation based on multidimensional telemetry.
- **U-Gamma Single Engine**: High-frequency cognitive pulse monitoring with cryptographically strong randomness via `secrets.SystemRandom`.
- **PQC WORM Logger**: Post-Quantum Cryptography (SHA3-512) Write-Once-Read-Many audit trail for multi-decade auditability.
- **Master Roadmap (2026–2035)**: A phased implementation plan for ZK-compliance, cognitive dead-man switches, and planetary-scale ASI alignment.

## 📂 Project Structure

- `engine/`: Core logic for risk scoring, cognitive pulsing, and audit logging.
- `tests/`: Integration and unit tests.
- `audit/`: Directory for WORM-protected audit logs.
- `omni_sentinel_24h_monitor.py`: Primary orchestration service.

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/onefinestarstuff/omni-sentinel.git
cd omni-sentinel

# Install dependencies (pytest for testing)
pip install pytest
```

## 🖥 Usage

### Running the Monitor
To start the 24-hour orchestration monitor:
```bash
python3 omni_sentinel_24h_monitor.py > monitor.log 2>&1 &
```

### Running Tests
```bash
python3 -m pytest tests/test_integration.py
```

## 🗺 Roadmap Highlights
- **2026-2028**: ZK-SNARKs for regulatory reporting and PQC Audit Trails.
- **2029-2031**: Cognitive Dead-Man Switches and Multi-Region TEE Mesh.
- **2032-2035**: Decentralized Omni-Sentinel Mesh for planetary alignment.

See [SENTINEL_G_MASTER_ROADMAP_2026_2035.md](SENTINEL_G_MASTER_ROADMAP_2026_2035.md) for the full roadmap.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.
