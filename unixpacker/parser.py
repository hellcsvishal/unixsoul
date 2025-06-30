class Command:
    def __init__(self, command, packages, flags):
        self.command = command
        self.packages = packages
        self.flags = flags
    def __repr__(self):
        return f"Command(command={self.command}, packages={self.packages}, flags={self.flags})"
    
    def parse_line(self,line):
        tokens=line.strip().split()
        if not tokens:
            return None
        
        command= tokens[0]
        packages = []
        flags = []

        for token in tokens[1:]:
            if token.startswith('-'):
                flags.append(token)
            else:
                packages.append(tokens)

        return Command(command, packages, flags)
    def parse_file(self,file_path):
        commands = []
        with open(file_path, 'r') as file:
            for line in file:
                command = self.parse_line(line)
                if command:
                    commands.append(command)
        return commands    

    def dic(self, text):
    dictionary = {}
    key = None
    buffer = []

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# [") and stripped.endswith("]"):
            if key is not None:
                dictionary[key] = "\n".join(buffer)
            key = stripped[3:-1].strip()  
            buffer = []
        elif key is not None and stripped and not stripped.startswith("#"):
            buffer.append(stripped)

    if key is not None:
        dictionary[key] = "\n".join(buffer)

    return dictionary
     