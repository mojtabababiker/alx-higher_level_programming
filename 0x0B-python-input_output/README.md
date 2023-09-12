# Python Input And Output

### Files can be considered the basic data stuctures on most of the operating systems, `python` like most of the other programing languages provides methods to work with files and all the files-like-wise objects, but before we move to this part there are some concepts we need to go through.


    1. **Files**: According to [Techopedia](https://www.techopedia.com/definition/7199/file) a file is a container for storing informations, the informations on the file determines the type of the file, ie.., `text files`, `data files` ...

    2. **Stream**: A stream is a sequence of bytes. In the `NFTS` fiel system, a stream contains the data that written to a file, and each stream associated with a file has its own allocating size, actual size, and valid data length, for more informations about [File Streams](https://learn.microsoft.com/en-us/windows/win32/fileio/file-streams).

    3. **Serialization**: Serialization is the process of converting an object’s state to a byte stream. This byte stream can then be saved to a file, sent over a network, or stored in a database. There are diffrents format to `serialize` a file you can look [here](https://www.baeldung.com/cs/serialization-deserialization) for more informations.


    4. **Deserialization**: Deserialization is the reverse process of serialization, for more information [here](https://www.baeldung.com/cs/serialization-deserialization). But here we will use `json` format for both `Serialization` and `Desrialization` for most of our ptojects.


