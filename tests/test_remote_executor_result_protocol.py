"""Regression contract for the Docker executor's sandbox-to-host result boundary."""

from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE = REPOSITORY_ROOT / "src/tools/executor/remote_executors.py"


def test_docker_executor_does_not_unpickle_kernel_stream_results():
    source = SOURCE.read_text(encoding="utf-8")

    assert "RESULT_PICKLE:" not in source
    assert "pickle.loads(base64.b64decode(pickle_data))" not in source
    assert "RESULT_JSON:" in source
    assert "json.loads(decoded_result.decode(\"utf-8\"))" in source


def test_result_protocol_binds_a_nonce_and_size_limit():
    source = SOURCE.read_text(encoding="utf-8")

    assert "secrets.token_urlsafe(24)" in source
    assert "MAX_RESULT_ENVELOPE_BYTES = 1_000_000" in source
    assert "base64.b64decode(result_data, validate=True)" in source
