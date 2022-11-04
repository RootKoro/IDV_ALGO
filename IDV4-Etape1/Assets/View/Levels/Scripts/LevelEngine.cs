using UnityEngine;

/// <summary>
/// Description : Level Engine to manage every level
/// @author : Louis PAKEL
/// </summary>
namespace IDV4.Common.Core
{
    public class LevelEngine : MonoBehaviour
    {
        #region Serialized Fields

        //[Header("CheckPoints")]
        //[SerializeField,Tooltip("Current CheckPoint")]
        //private CheckPoint _currentCheckPoint;

        #endregion

        #region Publics Properties

        // Singleton Instance
        public static LevelEngine Instance;

        #endregion

        #region Unity Methods

        private void Awake()
        {
            if (Instance == null)
            {
                Instance = this;
                DontDestroyOnLoad(this);
            }
            else
            {
                Destroy(this);
            }
        }

        #endregion

        #region Publics Methods

        #region Getter

        /// <summary>
        /// Decription : return the current checkpoint
        /// </summary>
        /// <returns></returns>
        //public CheckPoint GetCurrentCheckPoint()
        //{
        //    return _currentCheckPoint;
        //}

        #endregion

        #region Setter

        /// <summary>
        /// Description : Set the current checkpoint (last checkpoint reached) of the level
        /// </summary>
        /// <param name="pCheckPoint"></param>
        //public void SetCurrentCheckPoint(CheckPoint pCheckPoint)
        //{
        //    if(pCheckPoint != null)
        //    {
        //        _currentCheckPoint = pCheckPoint;
        //    }
        //}



        /// <summary>
        /// Description : Place the player to the spawner
        /// </summary>
        public void Spawn()
        {
            //GameEngine.Instance.GetPlayerGo().transform.position = _currentCheckPoint.GetSpawnArea().position;
        }

        #endregion

        #endregion
    }
}
