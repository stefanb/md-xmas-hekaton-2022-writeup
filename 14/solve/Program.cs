using System.Text;

const string text = "JB1SNB1kaXodMEQo";
const string key = "GqfAnI9NnC3L3yx1gNMn";


bool ValidatePassword(string pass)
{
    bool flag = string.IsNullOrEmpty(pass);
    bool result;
    if (flag)
    {
        result = false;
    }
    else
    {
        char[] array = new char[pass.Length];
        for (int i = 0; i < pass.Length; i++)
        {
            array[i] = (char)((ushort)pass[i] ^ (ushort)key[(i % key.Length)]);
        }
        string text3 = Convert.ToBase64String(Encoding.UTF8.GetBytes(array));
        bool flag2 = text == text3;
        result = flag2;
    }
    return result;
}

string GetPassword()
{
    var targetBytes=Convert.FromBase64String(text);
    string pass="";
    for (int i = 0; i < targetBytes.Length; i++)
    {
        pass += (char)((ushort)targetBytes[i] ^ (ushort)key[(i % key.Length)]);
    }
    return pass;
}


Console.WriteLine("Password: " + GetPassword());
Console.WriteLine("Valid:    " + ValidatePassword(GetPassword()));
