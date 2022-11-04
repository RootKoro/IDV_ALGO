using UnityEngine;

/// <summary>
/// Description : Game Engine
/// @author : Louis PAKEL
/// </summary>
namespace IDV4.Common.Core
{
    public class GameEngine : MonoBehaviour
    {
        #region Serialized Fields

        [Header("Player")]
        [SerializeField, Tooltip("Player Prefab")]
        private GameObject _playerPrefab;

        #endregion

        #region Publics Properties

        // Singleton Instance
        public static GameEngine Instance;

        #endregion

        #region Private Fields

        private GameObject _playerGo;
        //private PlayerController _playerController;
        //private MovementController _movementController;

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

        #region Public Methods

        /// <summary>
        /// Description : Load Player
        /// </summary>
        public void LoadPlayer()
        {
            if (_playerGo == null)
            {
                _playerGo = Instantiate(_playerPrefab, transform);

                //_playerController = _playerGo.transform.GetChild(0).GetComponent<PlayerController>();
                //_movementController = _playerGo.transform.GetChild(0).GetComponent<MovementController>();

                //_playerGo.name = _playerController.GetPlayer().GetName();
            }
        }

        public void ResetPlayer()
        {
            if (_playerGo != null)
            {
                Destroy(_playerGo.gameObject);
            }
                
            _playerGo = null;
            
            LoadPlayer();
        }


        /// <summary>
        /// Description : return the player gameobject
        /// </summary>
        /// <returns></returns>
        public GameObject GetPlayerGo()
        {
            return _playerGo;
        }


        ///// <summary>
        ///// Description : return the movement controller
        ///// </summary>
        ///// <returns></returns>
        //public MovementController GetMovementController()
        //{
        //    return _movementController;
        //}

        #endregion
    }
}