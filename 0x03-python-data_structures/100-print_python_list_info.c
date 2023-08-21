#include <Python.h>


void print_type(PyObject *p);
/**
 * print_python_list_info - print information about python list
 * @p: python list object
 */

void print_python_list_info(PyObject *p)
{
	unsigned long size, allocated, i;
	Py_ssize_t index;

	if (PyList_CheckExact(p))
	{
		index = 0;
		size = PyList_Size(p);
		allocated = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %lu\n", size);
		printf("[*] Allocated = %lu\n", allocated);
		for (i = 0 ; i < size ; i++)
		{
			printf("Element %lu: ", i);
			print_type(PyList_GetItem(p, index));
			index++;
		}
	}
}

/**
 * print_type - print the crossponding type name of the p type
 * @p: PyObject pointer
 */

void print_type(PyObject *p)
{
	char *type = NULL;
	/*PyObject_Print(p, stdout, 0);*/
	if (PyLong_CheckExact(p))
		type = "int";
	else if (PyFloat_CheckExact(p))
		type = "float";
	else if (PyComplex_CheckExact(p))
		type = "complex";
	else if (PyList_CheckExact(p))
		type = "list";
	else if (PyTuple_CheckExact(p))
		type = "tuple";
	else if (PyFrozenSet_CheckExact(p))
		type = "frozenset";
	else if (PyAnySet_CheckExact(p))
		type = "set";
	else if (PyDict_CheckExact(p))
		type = "dict";
	else if (PyUnicode_CheckExact(p)) /* str */
		type = "str";
	else if (PyBytes_CheckExact(p))
		type = "bytes";
	printf("%s\n", type);
}
