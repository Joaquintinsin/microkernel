# Microkernel Architectural Pattern
An example of microkernel architectural pattern use, from Software Engineer.

# Non-Modular example
Folder <u><i>/ejemplo_microkernel_unm</u></i> contains a single py file.

You can find the whole code of the modularized one, but cannot abstract of the single parts of the architectural pattern.

# Modular example
## <i>client.py</i>
File containing the client component of the pattern.
A client uses external modules operating the adapter component.

### /kernel
<center>
<b><i>module_interface.py</b></i>
</center>
Interface that external servers must implement in order to be registered properly in the microkernel.


<center>
<b><i>microkernel.py</b></i>
</center>
Core class, containing the communication between client, adapter, internal and external servers.
You can register a module and execute a module.


#### /kernel/internal
<center>
<b><i>error_handling_server.py</b></i>

<b><i>module_register_server.py</b></i>
</center>
Both files contains internal server classes.

Contains the logic to handle error or to register external modules to the microkernel.

### /externals
<center>
<b><i>addition_module.py</b></i>

<b><i>subtraction_module.py</b></i>
</center>
External servers.

Each class implements his own logic.

In case new externals wanted to be added to the program, it must implement <b>ModuleInterface</b>, be registered in the microkernel class and then an user is able to use that module as well as the others.


