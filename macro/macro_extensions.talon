macro remove [{user.saved_macros}]: user.macro_remove(saved_macros or "")
macro dump: user.macro_dump()
macro load: user.macro_load()