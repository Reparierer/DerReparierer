"""Auto-generate the index.rst files for all sub-folders for the sphinx toc-tree."""
import os


def generate_toc(base_path: str) -> list[str]:
    """
    Generate a list of all contents for the table of content (toc) tree.

    A content is a markdown file (file extension .md).

    :param base_path: base file path
    :type base_path: str
    :return: list of markdown files including relative file path
    :rtype: list[str]
    """
    toc_entries = []
    for dirpath, dirnames, filenames in os.walk(base_path, topdown=True):
        for filename in filenames:
            if filename.endswith('.md'):
                relative_path = os.path.relpath(os.path.join(dirpath, filename), base_path)
                toc_entries.append(relative_path)
    return toc_entries


if __name__ == "__main__":
    all_markdown_files = generate_toc('.')
    print(all_markdown_files)

    # generate a list of all base folders
    base_folder_list = []
    for md_filepath in all_markdown_files:
        base_folder = md_filepath.split("/")
        if base_folder[0] != "readme.md" and base_folder[0] not in base_folder_list:
            base_folder_list.append(base_folder[0])
    print(base_folder_list)

    base_folder_list = sorted(base_folder_list)

    # generate sub-index files
    for topic_folder in base_folder_list:
        index_string = (f"{topic_folder}\n"
                        f"==========================\n\n"
                        f".. toctree::\n"
                        f"   :maxdepth: 1\n"
                        f"   :caption: Contents:\n"
                        f"\n"
                        )

        for readme_file_name in all_markdown_files:
            # if topic_folder in readme_file_name:
            if readme_file_name.startswith(topic_folder):
                add_string_index = "   " + readme_file_name.replace(f"{topic_folder}/", "") + "\n"
                index_string += add_string_index

        with open(f"{topic_folder}/index.rst", "w") as text_file:
            text_file.write(index_string)

    # generate main-index file
    main_index_string = """Welcome to derReparierer. All about repairing electronics.
===============================================================================

Here you will find several categories for repairing electronic devices. Just take a look around!

.. toctree::
   :maxdepth: 1
   :caption: Repair Categories:
   :glob:
   
   readme.md
"""

    for topic_name in base_folder_list:
        add_main_string_index = f"   {topic_name}/index\n"
        main_index_string += add_main_string_index

    with open(f"index.rst", "w") as text_file:
        text_file.write(main_index_string)
