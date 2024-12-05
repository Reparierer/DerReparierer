"""Auto-generate the index.rst files for all sub-folders for the sphinx toc-tree."""
import os

# name convention:
# base_path / base_folder: project root directory
# topic: main topics, e.g. bike, car, computers, ...
# sub_topic: devices in a topic, e.g. mobile charger, subwoofer, radio inside the consumer electronics category
# toc_entry: every document that is part of the table of content (toc)
# md: markdown

# a markdown file is for every single device, e.g. mobile charger, subwoofer, radio inside the consumer electronics category

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
    toc_entries_md = generate_toc('.')
    print(toc_entries_md)

    # generate a list of all topics
    topic_list = []
    for single_md_filepath in toc_entries_md:
        topic_name_ = single_md_filepath.split("/")
        if topic_name_[0] != "readme.md" and topic_name_[0] not in topic_list:
            topic_list.append(topic_name_[0])
    # sort the topic list
    topic_list = sorted(topic_list)

    # generate index files for sub-topics
    for topic_folder in topic_list:
        # Note:
        # a maxdepth of 1 shows the sub-topics on sub-topic page
        # a maxdepth of 2 shows the subtopics and the captions inside the document (e.g. failure investigation).
        # -> 1 is preferred!
        sub_topic_index_string = (f"{topic_folder.replace("_", " ").title()}\n"
                        f"==========================\n\n"
                        f".. toctree::\n"
                        f"   :maxdepth: 1\n"
                        f"   :caption: Contents:\n"
                        f"\n"
                                  )
        # sort sub-topics by alphabet
        sub_topic_list = []
        for readme_file_name in toc_entries_md:
            if readme_file_name.startswith(topic_folder):
                sub_topic_list.append(readme_file_name.replace(f"{topic_folder}/", ""))
        sub_topic_list = sorted(sub_topic_list)

        # generate content for the sub-topic index.rst file
        for readme_file_name in sub_topic_list:
            add_string_index = "   " + readme_file_name + "\n"
            sub_topic_index_string += add_string_index

        # write sub-topic index.rst file
        with open(f"{topic_folder}/index.rst", "w") as text_file:
            text_file.write(sub_topic_index_string)

    # generate topic index.rst file
    # Note:
    # a maxdepth of 1 shows the topics on the landing page
    # a maxdepth of 2 shows the topics and subtopics on the landing page
    # a maxdepth of 3 shows the topics, subtopics and the captions inside the document (e.g. failure investigation).
    # -> 1 or 2 is preferred!
    main_index_string = """Welcome to derReparierer. All about repairing electronics.
===============================================================================

Here you will find several categories for repairing electronic devices. Just take a look around!

.. toctree::
   :maxdepth: 2
   :caption: Repair Categories:
   :glob:
   
   readme.md
"""
    # add dynamic topics to index.rst file
    for topic_name in topic_list:
        topic_string_index = f"   {topic_name}/index\n"
        main_index_string += topic_string_index

    # write main index.rst file
    with open(f"index.rst", "w") as text_file:
        text_file.write(main_index_string)
