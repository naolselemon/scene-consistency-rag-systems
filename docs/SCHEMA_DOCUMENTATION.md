# Schema Documentation

**Version**: 1.1

**Last Updated**: 2025-11-12

---

### Changelog

**v1.1 (2025-11-12)**
- **Added `entity_version` field** to Character and Location schemas to track canonical data revisions.
- **Added `setting` object** to Location schema for richer, structured scene context (time, weather, props).
- **Cleaned up `tags` enums** in Character and Location schemas to separate inherent traits from scene-specific context.

---

## Overview

This document provides comprehensive documentation for the core schemas in the Scene Consistency RAG system. Each schema is designed to maintain visual consistency of characters and locations across anime video generation scenes.

## Schema Files

| Schema | File | Purpose |
|--------|------|---------|
| **Character** | `schemas/character_schema.json` | Character attribute definitions |
| **Location** | `schemas/location_schema.json` | Location/world-building definitions |
| **Relationship** | `schemas/relationship_schema.json` | Individual relationship between entities |
| **Relationships Collection** | `schemas/relationships_collection_schema.json` | Collection of relationship objects |
| **Metadata** | `schemas/metadata_schema.json` | Shared metadata structure for all entities |

---

## Character Attribute Schema

### **File**: `schemas/character_schema.json` (v1.1)

### **Purpose**
Defines the structure for character data to ensure visual consistency across scenes.

### **Required Fields**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `character_id` | string | Unique identifier | `"char_isaac_001"` |
| `name` | string | Character name | `"Isaac"` |
| `canonical_image_path` | string | Reference image path | `"data/characters/isaac.png"` |
| `lora_trigger_word` | string | AI generation trigger | `"<lora:isaac_v1:1.0>"` |
| `appearance` | string | Visual description | `"white t-shirt, short brown hair"` |

### **Optional Fields**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `entity_version` | integer | Canonical version of the data record | `1`, `2` |
| `tags` | array | Inherent character traits | `["male", "protagonist", "human"]` |
| `embedding_id` | string | Vector embedding reference | `"emb_char_isaac_001"` |
| `metadata` | object | Provenance and timestamps | See metadata structure |

### **Validation Rules**

- `character_id`: Must match pattern `^char_[a-z_]+_\\d{3}$`.
- `canonical_image_path`: Must match pattern `^(data/characters/|https?://|s3://|gs://).+\.(jpg|jpeg|png|webp)$`.
- `lora_trigger_word`: Must match pattern `^<lora:[a-z0-9_]+_v\\d+(\\.\\d+)?:\\d+(\\.\\d+)?>$`.
- `appearance`: Must be 20-500 characters.
- `tags`: Must use the standardized taxonomy for inherent traits only: `male`, `female`, `non_binary`, `protagonist`, `antagonist`, `supporting`, `background`, `human`, `cybernetic`, `android`, `spiritual`.
- `entity_version`: Must be an integer >= 1.

### **Example Character**

```json
{
  "character_id": "char_isaac_001",
  "name": "Isaac",
  "entity_version": 1,
  "canonical_image_path": "data/characters/isaac.png",
  "lora_trigger_word": "<lora:isaac_v1:1.0>",
  "appearance": "Isaac, white t-shirt, short brown hair, athletic build, confident expression",
  "tags": ["male", "protagonist", "human"],
  "embedding_id": "emb_char_isaac_001",
  "metadata": {
    "source": "issac.txt",
    "created_at": "2025-11-07T14:00:00Z",
    "updated_at": "2025-11-12T10:00:00Z",
    "version": "1.1.0"
  }
}
```

---

## Location/World-Building Schema

### **File**: `schemas/location_schema.json` (v1.1)

### **Purpose**
Defines the structure for location data to ensure environmental consistency across scenes.

### **Required Fields**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `location_id` | string | Unique identifier | `"loc_office_001"` |
| `name` | string | Location name | `"Isaac's Office"` |
| `description` | string | Visual description | `"warmly lit office interior..."` |

### **Optional Fields**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `entity_version` | integer | Canonical version of the data record | `1`, `2` |
| `setting` | object | Default environmental context | `{"location": "office", "time_of_day": "daytime"}` |
| `type` | string | Location classification | `"indoor"` |
| `tags` | array | **Inherent location styles/types** | `["workspace", "urban", "modern"]` |
| `embedding_id` | string | Vector embedding reference | `"emb_loc_office_001"` |
| `canonical_image_path` | string | Reference image path | `"data/locations/office.jpg"` |
| `metadata` | object | Provenance and timestamps | See metadata structure |

### **Validation Rules**

- `location_id`: Must match pattern `^loc_[a-z_]+_\\d{3}$`.
- `description`: Must be 20-500 characters.
- `tags`: Must use the standardized taxonomy for **inherent styles only**: `residential`, `commercial`, `industrial`, `urban`, `suburban`, `rural`, `natural`, `modern`, `futuristic`, `traditional`, `abandoned`.
- `setting`: A nested object with its own properties (`location`, `time_of_day`, `weather`, `props`).
- `entity_version`: Must be an integer >= 1.

### **Example Location**

```json
{
  "location_id": "loc_office_001",
  "name": "Isaac's Office",
  "entity_version": 1,
  "description": "warmly lit office interior, wooden shelves and drawers, desk with monitor, large window with city skyline view",
  "type": "indoor",
  "tags": ["workspace", "urban", "modern"],
  "setting": {
    "location": "office",
    "time_of_day": "daytime",
    "weather": "sunny",
    "props": ["desk", "monitor", "window"]
  },
  "embedding_id": "emb_loc_office_001",
  "metadata": {
    "source": "manual_entry",
    "created_at": "2025-11-07T14:00:00Z",
    "updated_at": "2025-11-12T10:00:00Z",
    "version": "1.1.0"
  }
}
```
---

## Relationship Schema

### **File**: `schemas/relationship_schema.json`

### **Purpose**
Defines individual relationships between characters and locations for RAG retrieval filtering and reranking.

### **Required Fields**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `relationship_id` | string | Unique relationship identifier | `"rel_isaac_office_001"` |
| `source_entity` | string | Source entity ID | `"char_isaac_001"` |
| `target_entity` | string | Target entity ID | `"loc_office_001"` |
| `relationship_type` | string | Type of relationship | `"appears_in"` |

### **Optional Fields**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `strength` | number | Confidence/frequency (0.0-1.0) | `0.85` |
| `tags` | array | Descriptive tags | `["primary_setting", "work_context"]` |
| `metadata` | object | Shared metadata structure | See metadata schema |

### **Relationship Types**

- `appears_in` - Character appears in location
- `associated_with` - General association
- `interacts_with` - Character-character interaction
- `shares_theme` - Shared thematic elements

### **Validation Rules**

- `relationship_id`: Must match `^rel_[a-z_]+_\\d{3}$`
- `source_entity`/`target_entity`: Must match `^(char|loc)_[a-z_]+_\\d{3}$`
- `strength`: Must be between 0.0 and 1.0
- `relationship_type`: Must be one of defined types

### **Example Relationship**

```json
{
  "relationship_id": "rel_isaac_office_001",
  "source_entity": "char_isaac_001",
  "target_entity": "loc_office_001",
  "relationship_type": "appears_in",
  "strength": 0.85,
  "tags": ["primary_setting", "work_context"],
  "metadata": {
    "source": "script_analysis",
    "created_at": "2025-11-07T14:00:00Z",
    "updated_at": "2025-11-07T14:00:00Z",
    "version": "1.0",
    "confidence": 0.92,
    "validation_status": "validated"
  }
}
```

---


## Relationships Collection Schema

### **File**: `schemas/relationships_collection_schema.json`

### **Purpose**
Schema for collections of relationship objects, useful for bulk operations and database storage.

### **Required Fields**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `relationships` | array | Array of relationship objects | Array of relationship schemas |

### **Example Collection**

```json
{
  "relationships": [
    {
      "relationship_id": "rel_isaac_office_001",
      "source_entity": "char_isaac_001",
      "target_entity": "loc_office_001",
      "relationship_type": "appears_in",
      "strength": 0.85
    },
    {
      "relationship_id": "rel_isaac_gertie_001",
      "source_entity": "char_isaac_001",
      "target_entity": "char_gertie_001",
      "relationship_type": "interacts_with",
      "strength": 0.75
    }
  ]
}
```


## Shared Metadata Schema

### **File**: `schemas/metadata_schema.json`

### **Purpose**
Standardized metadata structure shared across all entity schemas for consistency and maintainability.

### **Fields**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `source` | string | Data origin | `"script_analysis"` |
| `created_at` | string | Creation timestamp | `"2025-11-07T14:00:00Z"` |
| `updated_at` | string | **Last data update** timestamp | `"2025-11-12T10:00:00Z"` |
| `version` | string | **Schema definition** version | `"1.1.0"` |
| `confidence` | number | Quality score (0.0-1.0) | `0.92` |
| `validation_status` | string | Validation state | `"validated"` |

### **Usage**
All entity schemas... reference this shared schema. This ensures a clear distinction between the **data version (`entity_version`)** and the **schema version (`metadata.version`)**.