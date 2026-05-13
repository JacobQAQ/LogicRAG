# LogicRAG

LogicRAG is an end-to-end prototype for logic-driven financial report generation.

## Pipeline

1. `document_learner.py`: extracts two state sequences, builds the global state template, and creates the state embedding index.
2. `query_processing.py`: embeds the user query, matches relevant states, and extracts a query-specific subtree.
3. `ifind_data_plugin.py`: retrieves data from iFinD and binds retrieved data to `required_materials`.
4. `report_generator.py`: generates the final report state by state while passing only a short previous-state summary as local context.
5. `logicrag_client.py`: user-friendly one-command client for the full pipeline.

## Environment Variables

You can either set environment variables in PowerShell:

```powershell
$env:DEEPSEEK_API_KEY="your_deepseek_key"
$env:DASHSCOPE_API_KEY="your_dashscope_key"
$env:DASHSCOPE_API_BASE="https://dashscope.aliyuncs.com/compatible-mode/v1"
$env:IFIND_USERNAME="your_ifind_username"
$env:IFIND_PASSWORD="your_ifind_password"
```

Or pass them directly to `logicrag_client.py` as CLI parameters.

## Input CSV Format

The CSV should contain at least two report rows:

```csv
report_id,section_1,section_2,section_3
report_a,text...,text...,text...
report_b,text...,text...,text...
```

Each row is treated as one sample report. The `report_id` column is optional but recommended.

## One-Command Run

```powershell
python logicrag_client.py `
  --csv "dataset\东吴证券\test\case_2253.csv" `
  --row-a 0 `
  --row-b 1 `
  --query "write a nonferrous metals research report for March 2, 2025" `
  --theta 0.5 `
  --tau 0.5 `
  --date "2025-02-28"
```

`theta` and `tau` default to `0.5`.

Use dry-run modes to check the pipeline without calling iFinD or the report-generation LLM:

```powershell
python logicrag_client.py --dry-run-data --dry-run-report
```

## Outputs

By default, outputs are written to `logicrag_outputs/`:

- `global_template.json`
- `state_index.json`
- `query_subtree.json`
- `retrieved_materials/`
- `generated_report.md`
- `generated_node_outputs.json`
- `generation_trace.json`
