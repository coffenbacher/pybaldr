# PyBaldr

PyBaldr is a library to interact with the Baldr serialization format 
(https://github.com/uswitch/baldr).

*Warning: very hastily put together. However, this should serve as a starting 
point. Pull requests welcomed.*

### Usage
Install the library:
   
    pip install pybaldr

Open a Baldr file and extract the records from it. This example has a few ints 
as records. Records can be any binary data:

    from pybaldr import full_read
    
    with open('tests/data/example.baldr', 'rb') as f:
        results = full_read(f.read())
    
    for r in results:
        print int(r.body)