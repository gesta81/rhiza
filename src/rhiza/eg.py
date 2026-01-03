def x():
    return 1


def greet(name: str = "World") -> str:
    """Greet a user with a friendly hello message.
    
    Args:
        name: The name to greet. Defaults to "World".
        
    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"