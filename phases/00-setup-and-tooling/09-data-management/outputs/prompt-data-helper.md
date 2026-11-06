# Dataset Selection Prompt

Use this prompt when choosing data for an AI task:

> I am building **[describe the task and intended users]**. The model will
> receive **[input type]** and should produce **[desired output]**. Recommend
> up to three datasets that fit this task. For each, give the Hugging Face Hub
> repository, data fields and labels, language, license, approximate size,
> available splits, and any privacy or access restrictions. Prefer a small,
> public dataset suitable for a first experiment. Explain how to load a small
> sample or stream it before downloading everything. Do not recommend using
> evaluation/test examples for training. Cite the dataset card for each claim.
