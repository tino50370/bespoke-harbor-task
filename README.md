# Bespoke Harbor Task

This project is a benchmarking framework for testing AI agents on complex software and DevOps problems. It utilizes the Harbor tool to run tasks multiple times, evaluate the agent's success rate, and provide reference solutions.

## Overview

The framework is designed to assess how well an AI agent can solve challenging technical problems, particularly in the DevOps domain. It runs a specified task a number of times (typically 10 runs) and tracks:
- How many times the agent successfully completes the task
- Detailed results and metrics from each run
- Reference solutions for comparison

## Current Task: Release Image Repair

This instance of the framework focuses on the `release_image_repair` task, a DevOps challenge involving repairing a broken CI release build for a containerized Python API.

### Task Description
The task requires repairing a misconfigured application repository so that:
- The service can start successfully from the repository root
- The `/health` endpoint returns the correct JSON payload with service identity and status
- The intended application behavior is preserved

### Task Structure
- `instruction.md`: Detailed task instructions
- `task.toml`: Task configuration and metadata
- `environment/`: Contains the broken repository and Docker setup
- `solution/`: Reference solution script (`solve.sh`)
- `tests/`: Test cases for validation

## Running the Framework

The project uses the Harbor tool for execution. Jobs are configured in the `jobs/` directory, with each subfolder representing a run.

### Example Job Structure
```
jobs/
  2026-04-01__12-00-56/
    config.json      # Job configuration
    result.json      # Run results
    release_image_repair__mJQ2DKZ/  # Task-specific artifacts
```

### Configuration
Jobs are configured via JSON files specifying:
- Number of attempts
- Agent settings
- Environment parameters
- Timeout multipliers
- Retry policies

## Results and Evaluation

After running the task multiple times, the framework provides:
- Success/failure statistics
- Detailed logs and artifacts from each run
- Comparison against the reference solution
- Metrics on agent performance

## Dependencies

- Python 3.12+
- Harbor tool
- Docker (for containerized environments)

## Usage

1. Set up the environment with required dependencies
2. Configure the job parameters in `config.json`
3. Run the Harbor tool to execute the benchmarking
4. Review results in the `jobs/` directory

This framework helps evaluate and improve AI agents' capabilities in solving real-world DevOps challenges.