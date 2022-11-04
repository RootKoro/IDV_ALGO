using UnityEngine;

/// <summary>
/// Description : Camera Controller Script
/// @author : Louis PAKEL
/// </summary>
namespace IDV4.Common.Controllers
{
    public class CameraController : MonoBehaviour
    {
        #region Serialized Fields

        [SerializeField] private Transform _target;
        [SerializeField] private float _lerpSpeed = 1.0f;

        #endregion

        #region Private Fiels

        private Vector3 _offset;

        private Vector3 _targetPos;

        #endregion

        #region Unity Methods

        private void OnEnable()
        {
            InitCameraController();
        }

        private void Update()
        {
            if (_target == null) return;

            _targetPos = _target.position + _offset;
            transform.position = Vector3.Lerp(transform.position, _targetPos, _lerpSpeed * Time.deltaTime);
        }

        #endregion

        #region Private Methods

        /// <summary>
        /// Description : Init Camera Controller
        /// </summary>
        private void InitCameraController()
        {
            _offset = transform.position - _target.position;

            transform.position = _target.position;
        }

        #endregion
    }
}
