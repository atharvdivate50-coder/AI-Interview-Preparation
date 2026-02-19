# ---------------------------------------------------------
# AI Interview Questions + Keywords Database (Major Project 1)
# ---------------------------------------------------------

questions_db = {
    "software engineer": {
        "google": [
            ("What is REST API?", ["api", "http", "client", "server", "request", "response"]),
            ("Explain OOPS concepts.", ["class", "object", "inheritance", "polymorphism", "encapsulation"]),
            ("Difference between list and tuple in Python?", ["list", "tuple", "mutable", "immutable", "ordered"]),
            ("What is abstraction?", ["abstraction", "interface", "hide", "implementation", "details"])
        ],
        "amazon": [
            ("What is time complexity?", ["algorithm", "time", "complexity", "efficient", "big O"]),
            ("Explain hashing.", ["hash", "function", "key", "value", "collision"]),
            ("Difference between stack and queue?", ["stack", "queue", "fifo", "lifo", "data structure"]),
            ("What is recursion?", ["recursion", "function", "call", "base case", "loop"])
        ],
        "tcs": [
            ("What is SDLC?", ["software", "development", "lifecycle", "requirement", "testing"]),
            ("Difference between compiler and interpreter?", ["compiler", "interpreter", "code", "execute", "translate"]),
            ("What is debugging?", ["debug", "error", "fix", "problem", "code"]),
            ("Explain Agile methodology.", ["agile", "sprint", "scrum", "iterations", "team"])
        ],
        "infosys": [
            ("What is loop?", ["loop", "iteration", "for", "while", "repeat"]),
            ("Explain variables.", ["variable", "store", "value", "name", "type"]),
            ("What is array?", ["array", "elements", "index", "size", "data structure"]),
            ("Difference between local and global variable?", ["local", "global", "scope", "variable", "function"])
        ],
        "microsoft": [
            ("What is a Memory Leak?", ["memory", "allocation", "leak", "pointer", "resource"]),
            ("Explain the concept of Middleware.", ["request", "response", "processing", "software", "layer"]),
            ("What is Dependency Injection?", ["dependency", "injection", "object", "coupling", "framework"])
        ],
        "meta": [
            ("What is a Hash Map?", ["key", "value", "hashing", "collision", "index"]),
            ("Explain Load Balancing.", ["traffic", "server", "distribution", "availability", "performance"]),
            ("What is a Deadlock in OS?", ["process", "resource", "waiting", "lock", "cycle"])
        ],
        "global": [
            ("What is a Pointer?", ["address", "memory", "variable", "reference"]),
            ("Explain the use of a Boolean.", ["true", "false", "logic", "condition"])
        ]
    },
    "data scientist": {
        "google": [
            ("What is Machine Learning?", ["data", "model", "algorithm", "learn", "prediction"]),
            ("What is overfitting?", ["training", "testing", "memorize", "generalize", "model"]),
            ("Difference between supervised and unsupervised learning?", ["supervised", "unsupervised", "labeled", "unlabeled", "algorithm"])
        ],
        "amazon": [
            ("What is regression?", ["regression", "predict", "dependent", "independent", "linear"]),
            ("What is classification?", ["classification", "categorize", "label", "target", "prediction"]),
            ("What is clustering?", ["clustering", "groups", "unsupervised", "similarity", "distance"])
        ],
        "tcs": [
            ("What is NumPy?", ["numpy", "array", "matrix", "efficient", "calculation"]),
            ("What is Pandas?", ["pandas", "dataframe", "series", "manipulation", "analysis"]),
            ("What is seaborn?", ["seaborn", "plot", "visualization", "style", "data"])
        ],
        "infosys": [
            ("What is data analysis?", ["analysis", "data", "patterns", "insights", "interpretation"]),
            ("What is visualization?", ["visualization", "chart", "graph", "plot", "data"]),
            ("What is data preprocessing?", ["preprocessing", "cleaning", "normalize", "transform", "prepare"])
        ],
        "global": [
            ("What is a p-value?", ["probability", "significance", "hypothesis", "test"]),
            ("Explain a Normal Distribution.", ["bell curve", "mean", "standard deviation", "symmetrical"])
        ]
    },
    "web developer": {
        "google": [
            ("What is the DOM?", ["document", "object", "model", "html", "javascript", "tree"]),
            ("Explain CSS Flexbox.", ["flex", "layout", "container", "align", "justify", "direction"]),
            ("What is a closure in JavaScript?", ["closure", "scope", "function", "inner", "outer", "variables"])
        ],
        "amazon": [
            ("What is Responsive Design?", ["media queries", "mobile", "layout", "flexible", "viewport"]),
            ("Explain the difference between GET and POST.", ["method", "http", "data", "url", "body", "security"]),
            ("What is localStorage?", ["storage", "browser", "client", "persistent", "data", "key"])
        ],
        "tcs": [
            ("What is HTML5?", ["markup", "semantic", "tags", "video", "canvas", "header"]),
            ("What is the purpose of CSS?", ["style", "design", "layout", "presentation", "appearance"]),
            ("Difference between ID and Class in CSS?", ["unique", "reusable", "selector", "priority", "styling"])
        ],
        "global": [
            ("What is an API?", ["interface", "request", "data", "server"]),
            ("What is a Frontend framework?", ["react", "angular", "vue", "library", "ui"])
        ]
    },
    "java developer": {
        "google": [
            ("What is the JVM?", ["java", "virtual", "machine", "bytecode", "execution", "platform"]),
            ("Explain Java Collections Framework.", ["list", "set", "map", "interface", "classes", "collection"]),
            ("What is multithreading?", ["thread", "parallel", "execution", "concurrency", "process"])
        ],
        "amazon": [
            ("What is an Abstract Class?", ["abstraction", "method", "extend", "implementation", "partial"]),
            ("Explain the 'final' keyword.", ["constant", "variable", "method", "class", "cannot", "change"]),
            ("What is Hibernate?", ["orm", "database", "mapping", "framework", "java", "sql"])
        ],
        "tcs": [
            ("What is a Constructor?", ["initialize", "object", "class", "method", "name"]),
            ("Difference between Array and ArrayList?", ["size", "fixed", "dynamic", "collection", "type"]),
            ("What is Exception Handling?", ["try", "catch", "throw", "error", "runtime", "flow"])
        ],
        "global": [
            ("What is an Object?", ["instance", "class", "state", "behavior"]),
            ("Explain Method Overloading.", ["parameter", "signature", "same name", "different"])
        ]
    },
    "python developer": {
        "google": [
            ("What is a Decorator in Python?", ["function", "modify", "wrapper", "behavior", "closure"]),
            ("Explain Python's GIL.", ["global", "interpreter", "lock", "thread", "concurrency"]),
            ("What are Generators?", ["yield", "iterator", "memory", "efficient", "lazy"])
        ],
        "tcs": [
            ("What is a Lambda function?", ["anonymous", "small", "oneline", "expression"]),
            ("Difference between __init__ and __str__?", ["constructor", "string", "representation", "method"]),
            ("Explain Pip.", ["package", "manager", "install", "library", "module"])
        ],
        "global": [
            ("What is a Dictionary?", ["key", "value", "pair", "mutable"]),
            ("Explain indentation in Python.", ["block", "structure", "whitespace", "syntax"])
        ]
    },
    "cybersecurity analyst": {
        "microsoft": [
            ("What is Phishing?", ["email", "fraud", "deceive", "credentials", "malicious"]),
            ("Explain the OSI Model.", ["layer", "network", "communication", "protocol", "physical"]),
            ("What is a Firewall?", ["security", "traffic", "filter", "network", "barrier"])
        ],
        "amazon": [
            ("What is Encryption?", ["data", "secure", "key", "plaintext", "ciphertext"]),
            ("Explain DDoS attack.", ["distributed", "denial", "service", "traffic", "overflow"]),
            ("What is MFA?", ["multi", "factor", "authentication", "security", "identity"])
        ],
        "global": [
            ("What is a Virus?", ["malware", "replicate", "harm", "software"]),
            ("Explain Social Engineering.", ["psychological", "manipulation", "human", "error", "security"])
        ]
    }
}

# ---------------------------------------------------------
# Function: Get all questions + keywords for role + company
# ---------------------------------------------------------
def get_all_questions(role, company):
    role = role.lower().strip()
    company = company.lower().strip()
    
    # 1. Check for specific Role + Company
    if role in questions_db and company in questions_db[role]:
        return questions_db[role][company]
    
    # 2. Failsafe: If company not found, return general questions for that role
    elif role in questions_db and "global" in questions_db[role]:
        return questions_db[role]["global"]
        
    # 3. If nothing matches
    return []
