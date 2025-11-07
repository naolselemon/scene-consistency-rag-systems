# Scene Consistency RAG System

A Retrieval-Augmented Generation (RAG) system for maintaining scene consistency in anime video generation pipelines.

## Overview

This system provides contextual character and location information to video generation prompts, ensuring visual consistency across scenes.

## Features

-  **Character Consistency**: Canonical appearance + LoRA triggers
- ️ **Location Consistency**: Visual descriptions for environments

## Quick Start

```bash
# Clone and setup
cd scene-consistency-rag-systems
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Validate schemas
python scripts/validate_schemas.py --schema schemas/character_schema.json --data examples/character_example.json
```

## Project Structure

```
scene-consistency-rag-systems/
├── data/
│   └── characters/              # Character reference text (images excluded)
├── schemas/                     # JSON schema definitions
│   ├── character_schema.json
│   ├── location_schema.json
│   ├── relationship_schema.json
│   ├── relationships_collection_schema.json
│   └── metadata_schema.json
├── examples/                    # Example data files
│   ├── character_example.json
│   ├── location_example.json
│   ├── relationship_example_new.json
│   └── relationships_collection_example.json
├── docs/                        # Documentation
│   ├── SCHEMA_DOCUMENTATION.md
│   └── EMBEDDING_STRATEGY.md
├── src/scene_consistency/       # Main package
├── scripts/                     # Utility scripts
└── requirements.txt             # Dependencies
```

**Note**: Character reference images are excluded from Git (see .gitignore) to keep repository lightweight.

## Schemas

### Character Schema

**File**: `schemas/character_schema.json`

**Required fields (5)**:
```json
{
  "character_id": "char_isaac_001",
  "name": "Isaac",
  "canonical_image_path": "data/characters/isaac.png",
  "lora_trigger_word": "<lora:isaac_v1:1.0>",
  "appearance": "Isaac, white t-shirt, short brown hair, athletic build"
}
```

**Purpose**: Provides canonical visual appearance and generation triggers.

### Location Schema

**File**: `schemas/location_schema.json`

**Required fields (3)**:
```json
{
  "location_id": "loc_office_001",
  "name": "Isaac's Office",
  "description": "warmly lit office interior, wooden shelves, desk, city window"
}
```

**Purpose**: Provides consistent environment descriptions.

### Relationship Schema

**Files**:
- `schemas/relationship_schema.json` - Individual relationships
- `schemas/relationships_collection_schema.json` - Relationship collections  
- `schemas/metadata_schema.json` - Shared metadata structure

Defines relationships between entities with quantitative strength for RAG filtering and reranking.

## Validation

```bash
# Validate character data
python scripts/validate_schemas.py --schema schemas/character_schema.json --data examples/character_example.json

# Validate location data
python scripts/validate_schemas.py --schema schemas/location_schema.json --data examples/location_example.json

# Validate relationship data
python scripts/validate_schemas.py --schema schemas/relationship_schema.json --data examples/relationship_example_new.json

# Validate relationships collection
python scripts/validate_schemas.py --schema schemas/relationships_collection_schema.json --data examples/relationships_collection_example.json
```

## Documentation

- **[Schema Documentation](docs/SCHEMA_DOCUMENTATION.md)**: Complete schema reference
- **[Embedding Strategy Research](docs/EMBEDDING_STRATEGY.md)**: Research analysis for Phase 2 retrieval system

## Characters

- **Isaac**: Male protagonist, normal human
- **Gertie**: Female protagonist, normal human
- **Baolin**: Male character, cybernetic (energy blades, flight)
- **Fengwu**: Female character, energy wielder (energy whips)
- **Jianlong**: Male character, superhuman (super strength)
- **Mingfei**: Female character, cybernetic/spiritual (teal energy)
