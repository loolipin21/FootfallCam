import os
import shutil
import re

# Folders
frames_dir = 'frames'
labeled_images_dir = 'project-1-at-2025-06-09-15-38-13329773/images'
labeled_labels_dir = 'project-1-at-2025-06-09-15-38-13329773/labels'
output_img_dir = 'badge_dataset/images'
output_lbl_dir = 'badge_dataset/labels'

os.makedirs(output_img_dir, exist_ok=True)
os.makedirs(output_lbl_dir, exist_ok=True)

# Step 1: Copy & rename labeled files
pattern = re.compile(r"(\d+)(?=\.\w+$)")

labeled_count = 0
for fname in os.listdir(labeled_images_dir):
    match = pattern.search(fname)
    if not match:
        continue
    frame_id = match.group(1).zfill(5)

    # Copy image
    shutil.copy(os.path.join(labeled_images_dir, fname),
                os.path.join(output_img_dir, f"{frame_id}.jpg"))

    # Copy matching label
    label_name = fname.replace(".jpg", ".txt")
    shutil.copy(os.path.join(labeled_labels_dir, label_name),
                os.path.join(output_lbl_dir, f"{frame_id}.txt"))
    labeled_count += 1

print(f"✅ Copied and renamed {labeled_count} labeled files")

# Step 2: Copy all frames & fill blanks for unlabeled ones
frame_files = [f for f in os.listdir(frames_dir) if f.endswith(".jpg")]
blank_count = 0
for fname in frame_files:
    if not os.path.exists(os.path.join(output_img_dir, fname)):
        shutil.copy(os.path.join(frames_dir, fname),
                    os.path.join(output_img_dir, fname))

    lbl_path = os.path.join(output_lbl_dir, fname.replace(".jpg", ".txt"))
    if not os.path.exists(lbl_path):
        open(lbl_path, 'w').close()
        blank_count += 1

print(f"✅ Added {blank_count} blank label files")
