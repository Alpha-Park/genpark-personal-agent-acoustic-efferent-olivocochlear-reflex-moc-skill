"""
MCP Server for Medial Olivocochlear (MOC) Efferent Acoustic Reflex Skill.
Conforms to Model Context Protocol (MCP) JSON-RPC 2.0 stdio specification.
"""

import sys
import json
from client import MedialOlivocochlearReflexClient


def handle_request(line: str) -> None:
    try:
        req = json.loads(line)
    except Exception:
        return

    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {
                    "name": "genpark-personal-agent-acoustic-efferent-olivocochlear-reflex-moc-skill",
                    "version": "1.0.0"
                }
            }
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()
    elif method == "tools/list":
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "evaluate_moc_suppression",
                        "description": "Calculate MOC efferent OAE suppression delta (dB), linear damping %, and cochlear outer hair cell protection.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "baseline_oae_amplitude_db_spl": {"type": "number", "description": "Baseline OAE amplitude in quiet (dB SPL)."},
                                "suppressed_oae_amplitude_db_spl": {"type": "number", "description": "OAE amplitude during contralateral noise (dB SPL)."},
                                "cas_noise_level_db_spl": {"type": "number", "description": "Contralateral noise stimulus level (default: 60.0 dB SPL)."},
                                "frequency_hz": {"type": "number", "description": "Frequency in Hz (default: 2000.0 Hz)."},
                                "baseline_noise_floor_db_spl": {"type": "number", "description": "Noise floor in dB SPL (default: -20.0)."}
                            },
                            "required": ["baseline_oae_amplitude_db_spl", "suppressed_oae_amplitude_db_spl"]
                        }
                    }
                ]
            }
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "evaluate_moc_suppression":
            client = MedialOlivocochlearReflexClient()
            try:
                res = client.evaluate_moc_suppression(
                    baseline_oae_amplitude_db_spl=float(args["baseline_oae_amplitude_db_spl"]),
                    suppressed_oae_amplitude_db_spl=float(args["suppressed_oae_amplitude_db_spl"]),
                    cas_noise_level_db_spl=float(args.get("cas_noise_level_db_spl", 60.0)),
                    frequency_hz=float(args.get("frequency_hz", 2000.0)),
                    baseline_noise_floor_db_spl=float(args.get("baseline_noise_floor_db_spl", -20.0))
                )
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
                    }
                }
            except Exception as e:
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32000, "message": str(e)}
                }
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
    else:
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {"code": -32601, "message": f"Method {method} not found"}
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()


def main():
    for line in sys.stdin:
        if line.strip():
            handle_request(line)


if __name__ == "__main__":
    main()
