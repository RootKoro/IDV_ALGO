
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    [SerializeField]
    private int _gems;
    [SerializeField]
    private int _orbs;
    [SerializeField]
    private int _symbols;
    [SerializeField]
    private int _level;
    [SerializeField]
    private string _name;
    [SerializeField]
    private float _experiences;
    private float _maxExperiences;
     
  

// Retourne le nombre total de gemmes possédées par le joueur
public int GetGems()
{
     return this._gems;

}
   

// Ajoute des gemmes à celles possédées par le joueur
public void AddGem(int pGem)
{
    this._gems = this._gems + pGem;
}

// Définit le nombre de gemmes possédées par le joueur
private void SetGems(int pGems)
{
     this._gems = pGems;
}
    

// Retourne le nombre total d'orbes possédés par le joueur
public int GetOrbs()
{
    return this._orbs;
}

// Ajoute des orbes à ceux possédés par le joueur
public void AddOrb(int pOrb)
{
    this._orbs = this._orbs + pOrb;
}

// Définit le nombre d'orbes possédés par le joueur
private void SetOrbs(int pOrbs)
{
    this._orbs = pOrbs;
}

// Retourne le nombre total de symboles possédés par le joueur
public int GetSymbols()
{
    return this._symbols;
}

// Ajoute des symboles à ceux possédés par le joueur
public void AddSymbol(int pSymbol)
{
    this._symbols = this._symbols + pSymbol;
}

// Définit le nombre de symboles possédés par le joueur
private void SetSymbols(int pSymbols)
{
    this._symbols = pSymbols;
}

// Retourne le niveau actuel du joueur
public int GetLevel()
{
    return this._level;
}


// Définit le niveau du joueur
private void SetLevel(int pLevel)
{
    this._level = pLevel;
}

// Retourne le nom du joueur
public string GetName()
{
    return this._name;
}

// Retourne l'expérience acquise par le joueur
public float GetExperiences()
{
    return this._experiences;
}

// Ajoute de l'expérience au joueur
public void AddExperiences(float pExperience)
{
    this._experiences = this._experiences + pExperience;
}

// Définit l'expérience acquise par le joueur
private void SetExperiences(float pExperiences)
{
    this._experiences = pExperiences;
}

// Retourne l'expérience requise pour atteindre le prochain niveau
public float GetMaxExperiences()
{
    return this._maxExperiences;
}

// Définit l'expérience maximum à avoir pour atteindre le prochain niveau du joueur
private void SetMaxExperiences(float pMaxExperiences)
{
    this._maxExperiences = pMaxExperiences;
}

// Vérifie si le joueur peut augmenter de niveau, c'est-à-dire si l'expérience requise est atteinte ou dépassée.
private bool IsReadyToLevelUp()
{
    if  (this._experiences >= this._maxExperiences);
    return true ;

}

// Augmente le niveau du joueur et le nombre max d'expérience à avoir pour le prochain niveau.
// Si le joueur possède plus d'expérience que nécessaire, l'excédent s'ajoute au nouveau niveau.
private void LevelUp()
{
    if (IsReadyToLevelUp()){
        this._level++;
    }
}

// Retourne le script player sous format string
public override string ToString()
{
    return "gem :" + this._gems +
            "orbs :" +  this._orbs +
            "symbols :" + this._symbols+
            "level :" + this._level +
            "name :" + this._name +
             "experiences : " + this._experiences +
             "maxExperiences : " + this._maxExperiences;
}

}
