#!/usr/bin/env python3
"""
Schema validation script for Scene Consistency RAG System.

Validates JSON data against schema definitions.
"""

import json
import sys
import argparse
from pathlib import Path
from jsonschema import validate, ValidationError, SchemaError

def load_schema(schema_path: Path) -> dict:
    """Load JSON schema from file."""
    try:
        with open(schema_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f" Schema file not found: {schema_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f" Invalid JSON in schema {schema_path}: {e}")
        sys.exit(1)

def load_data(data_path: Path) -> dict:
    """Load JSON data from file."""
    try:
        with open(data_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f" Data file not found: {data_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f" Invalid JSON in data {data_path}: {e}")
        sys.exit(1)

def validate_data(data: dict, schema: dict, data_path: Path) -> bool:
    """Validate data against schema."""
    try:
        validate(instance=data, schema=schema)
        print(f" {data_path.name} is valid")
        return True
    except ValidationError as e:
        print(f" {data_path.name} validation failed:")
        print(f"   Error: {e.message}")
        if e.path:
            print(f"   Path: {' -> '.join(str(p) for p in e.path)}")
        return False
    except SchemaError as e:
        print(f" Schema error: {e.message}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Validate JSON data against schemas")
    parser.add_argument("--schema", required=True, help="Path to schema file")
    parser.add_argument("--data", required=True, help="Path to data file")
    
    args = parser.parse_args()
    
    schema_path = Path(args.schema)
    data_path = Path(args.data)
    
    print(f" Validating {data_path.name} against {schema_path.name}")
    
    # Load schema and data
    schema = load_schema(schema_path)
    data = load_data(data_path)
    
    # Validate
    is_valid = validate_data(data, schema, data_path)
    
    if is_valid:
        print(" Validation successful!")
        sys.exit(0)
    else:
        print(" Validation failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
