using System;

// Manager class (Reference Type)
class Manager
{
    public string Name { get; set; }
    public Manager(string name)
    {
        Name = name;
    }

    // Deep copy method for Manager
    public Manager Clone()
    {
        return new Manager(this.Name);
    }
}

// Department class
class Department
{
    public string Name { get; set; }
    public Manager Manager { get; set; }

    public Department(string name, Manager manager)
    {
        Name = name;
        Manager = manager;
    }

    // Shallow Copy (Copies reference, not object)
    public Department ShallowCopy()
    {
        return (Department)this.MemberwiseClone();
    }

    // Deep Copy (Creates a new Manager instance)
    public Department DeepCopy()
    {
        return new Department(this.Name, this.Manager.Clone());
    }
}
