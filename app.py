import csv
from collections import Counter

DATASET_FILE = "annotation_dataset.csv"
OUTPUT_FILE = "completed_annotations.csv"

annotations = []

print("\n" + "=" * 60)
print("AI ANNOTATION & QUALITY ASSURANCE PLATFORM")
print("=" * 60)

with open(DATASET_FILE, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("\n" + "-" * 50)
        print(f"Record ID: {row['ID']}")
        print(f"Text: {row['Text']}")

        label = input(
            "\nLabel (Positive / Neutral / Negative): "
        ).strip()

        confidence = int(
            input("Confidence Score (0-100): ")
        )

        reason = input("Annotation Reason: ")

        reviewer = input("Reviewer Name: ")

        approval = input(
            "Approve Annotation? (Yes/No): "
        ).strip()

        annotations.append({
            "ID": row["ID"],
            "Text": row["Text"],
            "Label": label,
            "Confidence": confidence,
            "Reason": reason,
            "Reviewer": reviewer,
            "Approval": approval
        })

with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "ID",
        "Text",
        "Label",
        "Confidence",
        "Reason",
        "Reviewer",
        "Approval"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(annotations)

print("\nAnnotations saved successfully.")

print("\nGenerating Quality Report...")

label_counts = Counter(
    item["Label"]
    for item in annotations
)

average_confidence = (
    sum(
        item["Confidence"]
        for item in annotations
    )
    / len(annotations)
)

approved = sum(
    1
    for item in annotations
    if item["Approval"].lower() == "yes"
)

approval_rate = (
    approved / len(annotations)
) * 100

print("\n" + "=" * 60)
print("QUALITY ASSURANCE REPORT")
print("=" * 60)

print(f"Total Records: {len(annotations)}")
print(f"Average Confidence: {average_confidence:.2f}%")
print(f"Approval Rate: {approval_rate:.2f}%")

print("\nLabel Distribution:")

for label, count in label_counts.items():
    print(f"{label}: {count}")

print("\nDataset Review Complete.")
