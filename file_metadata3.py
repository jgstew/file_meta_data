"""script to test hachoir metadata parsing"""

import hachoir.metadata
import hachoir.parser


def main():
    """execution starts here"""
    print("main():")
    filepath = r"C:\Program Files\7-Zip\7z.exe"
    parser = hachoir.parser.createParser(str(filepath))

    metadata = hachoir.metadata.extractMetadata(parser)

    # See what keys you can extract
    # https://stackoverflow.com/questions/14546533/hachoir-retrieving-data-from-a-group
    for k in metadata._Metadata__data:
        if k:
            # print(k) # print all keys
            if metadata.has(k):
                print(f"key: `{k}`  value:")
                for x in metadata.getValues(k):
                    print(x)


    print("\n")
    print(metadata.get("comment", index=0))

    print(metadata.getItem("comment", index=0))

    print(metadata.__iter__)

    print(metadata)

    metadata_dict = metadata.exportDictionary()["Metadata"]

    for k, v in metadata_dict.items():
        print(f"key: `{k}`  Value: `{v}`")

    print(metadata_dict["Creation date"])

    #array:
    print(metadata.getValues("creation_date"))

    for x in metadata.getValues("creation_date"):
        print(x)


if __name__ == "__main__":
    main()
