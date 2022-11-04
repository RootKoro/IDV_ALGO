public interface ICheckPoint
{
    void save();
    void ResetCheckPoint();
    void Load();
}