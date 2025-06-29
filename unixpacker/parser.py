class Command:
    def __init__(self, command, packages, flags):
        self.command = command
        self.packages = packages
        self.flags = flags
    def __repr__(self):
        return f"Command(command={self.command}, packages={self.packages}, flags={self.flags})"
    
    def parse_line(self,line):
        tokens=line.strip().split()
        if not toknns:
            return None
        
        command= tokens[0]
        packages = []
        flags = []

        for tokens in tokens[1:]:
            if tokens.startswith('-'):
                flags.append(tokens)
            else:
                packages.append(tokens)

        return Command(command, packages, flags)
    def psre_file(self,file_path):
        commands = []
        with open(file_path, 'r') as file:
            for line in file:
                command = self.parse_line(line)
                if command:
                    commands.append(command)
        return commands    