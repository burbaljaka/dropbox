import dropbox
import posixpath
from dropbox.exceptions import ApiError


def process_folder_entries(current_state, entries):
    for entry in entries:
        if isinstance(entry, dropbox.files.FileMetadata):
            current_state[entry.path_lower] = entry
        elif isinstance(entry, dropbox.files.DeletedMetadata):
            current_state.pop(entry.path_lower, None)  # ignore KeyError if missing
    return current_state


def path_exists(path):
    try:
        dbx.files_get_metadata(path)
        return True
    except ApiError as e:
        if e.error.get_path().is_not_found():
            return False
        raise




print("Initializing Dropbox API...")
dbx = dropbox.Dropbox("<ACCESS TOKEN>")

print("Scanning for expense files...")
result = dbx.files_list_folder(path="")
files = process_folder_entries({}, result.entries)

# check for and collect any additional entries
while result.has_more:
    print("Collecting additional files...")
    result = dbx.files_list_folder_continue(result.cursor)
    files = process_folder_entries(files, result.entries)

for entry in files.values():
    # use modified time of file to build destination path
    destination_path = posixpath.join(
        "/" + str(entry.client_modified.year) + "_Expenses",
        str(entry.client_modified.month)
    )

    # check to see if we need to create the destination folder
    if not path_exists(destination_path):
        print("Creating folder: {}".format(destination_path))
        dbx.files_create_folder_v2(destination_path)

    print("Moving {} to {}".format(entry.path_display, destination_path))
    dbx.files_move_v2(entry.path_lower, destination_path + "/" + entry.name)
print("Complete!")