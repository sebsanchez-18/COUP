##THIS IS FOR THE CARD OBJECTS AND CLASS##
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Set, Optional
import uuid

class Role(str,Enum):
    DUKE = "Duke"
    ASSASSIN = "Assassin"
    AMBASSADOR = "Ambassador"
    CAPTAIN = "Captain"
    CONTESSA = "Contessa"
    
    @staticmethod   
    def from_string(value: str) -> "Role":
            """Lenient parse for user/dev input."""
            v = value.strip().lower()
            mapping = {
                "duke": Role.DUKE,
                "assassin": Role.ASSASSIN,
                "captain": Role.CAPTAIN,
                "ambassador": Role.AMBASSADOR,
                "contessa": Role.CONTESSA,
            }
            if v not in mapping:
                raise ValueError(f"Unknown role: {value}")
            return mapping[v]
## Actions
ACTION_TAX = "tax"
ACTION_FOREIGN_AID = "foreign_aid"
ACTION_COUP = "coup"
ACTION_ASSASSINATE = "assassinate"
ACTION_EXCHANGE = "exchange"
ACTION_STEAL = "steal"

## Block actions
BLK_FOREIGN_AID = "block_foreign_aid"     
BLK_ASSASSINATE = "block_assassinate"     
BLK_STEAL = "block_steal"                


RoleActions: Dict[Role, Set[str]] = {    
   

    

def __init_():
